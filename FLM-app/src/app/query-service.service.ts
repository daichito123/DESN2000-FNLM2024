import { Injectable } from '@angular/core';

// To run model
import { AutoTokenizer } from '@xenova/transformers';
import * as tf from '@tensorflow/tfjs';

type GraphObject = {
  X_AXIS_LABEL: string;
  Y_AXIS_LABEL: string;
  PLOT_TYPE: string;
};

@Injectable({
  providedIn: 'root',
})
export class QueryServiceService {
  private queries: string[] = [];
  private fileEvent: any;
  private currentFile: any;
  public chart: any;
  private currentFileName: string = 'No File Uploaded';
  public parsedData: any;
  public loading: boolean = false;

  getQueries(): string[] {
    return [...this.queries]; // Return a copy of the array for immutability
  }

  getCurrentQuery(): string {
    return this.queries[this.queries.length - 1];
  }

  addQuery(newQuery: string) {
    this.queries.push(newQuery);
  }

  getCurrentFile() {
    return this.currentFile
  }


  addFileEvent(fileEvent: any) {
    this.loading = true;
    this.fileEvent = fileEvent;
    this.currentFile = fileEvent.target.files[0];
    this.currentFileName = this.currentFile.name;

    // this.readFile()
  }

  readFile(){
    let fileReader = new FileReader();
    fileReader.onload = (e) => {
      let lines: string[];
      if (typeof fileReader.result === 'string') {
        lines = fileReader.result.split('\n');
        this.parseData(lines)
        this.loading = false;
        console.log("FINISHED DATA READING")
      } else {
        console.error('Unexpected data type. Please provide a string.');
        return;
      }
    };

    fileReader.readAsText(this.currentFile);
  }

  parseData(lines: string[]) {
    const columnNames = lines[0].split(',');
    const allStrings = columnNames.every((name) => typeof name === 'string');
    if (!allStrings) {
      console.error('Error: Column names contain non-string values.');
      return;
    }

    const data: { [key: string]: string[]; } = {};
    for (let i = 1; i < lines.length-1; i++) {
      const values = lines[i].split(',');
      
      data[values[0]] = [];
      for (let j = 1; j < values.length; j++) {
        const trimmedValue = values[j].split('\r')[0]
        data[values[0]].push(trimmedValue);
      }
    }
    this.parsedData = data
  }

  getFileName(): string {
    return this.currentFileName;
  }

  // ML functions
  
  async mlPredict(query:string):Promise<GraphObject>{
    // Load model and tokenizer
    const model_name = 'ditto123/FNLM-DESN200';
    const tokenizer = await AutoTokenizer.from_pretrained(model_name);
    console.log("Checkpoint1")
    const model_path = '/assets/tfjs_model/model.json';
    const model = await tf.loadLayersModel(model_path);

    console.log("Checkpoint2")

    // Tokenize input text
    const inputs = tokenizer.encode(query);
    const tensors = tf.tensor(inputs);

    // Get tokens from input IDs
    const tokens = tokenizer.decode(inputs).split(' ');

    // Run model
    const outputs = model.predict(tensors) as tf.Tensor;
    const logits = outputs.arraySync()

    const predictions = tf.argMax(logits, -1).arraySync();

    console.log(predictions)

    const labelMap: { [key: number]: string } = {
      0: "O",
      1: "B-PLOT_TYPE",
      2: "I-PLOT_TYPE",
      3: "B-X_AXIS_LABEL",
      4: "I-X_AXIS_LABEL",
      5: "B-Y_AXIS_LABEL",
      6: "I-Y_AXIS_LABEL"
    };
    
    const predictedLabels = predictions[].map((label: any) => labelMap[label.item()]);
    
    // Remove items with 'O' Tag
    const filteredResults = tokens.map((token: string, idx: number) => ({
      token,
      label: predictedLabels[idx]
    })).filter(item => item.label !== 'O');
    
    // Remove B and O tags
    const cleanedResults = filteredResults.map(({ token, label }) => ({
      token,
      label: label.replace('B-', '').replace('I-', '')
    }));
    
    // Group by NER_TAG
    const data: { [key: string]: string } = {};
    cleanedResults.forEach(({ token, label }) => {
    if (!(label in data)) {
      data[label] = '';
    }
    if (token.includes('#')) {
      data[label] = (data[label] + token).replace('#', '');
    } else {
      data[label] += token;
    }
    });
    
    // Standardize plot type
    const plotTypeKey = 'PLOT_TYPE';
    if (new RegExp('scatter', 'i').test(data[plotTypeKey])) {
    data[plotTypeKey] = 'SCATTER';
    }
    
    // Capitalize everything
    for (const [key, value] of Object.entries(data)) {
      data[key] = value.toUpperCase();
    }
      return {
      X_AXIS_LABEL: 'ACOX2 (Liver)',
      Y_AXIS_LABEL: 'KCNE4 (Heart)',
      PLOT_TYPE: 'scatter',
    };
  }
}
