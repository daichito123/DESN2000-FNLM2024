import { Injectable } from '@angular/core';


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

  mlPredict(query:string):GraphObject{
    console.log(query)

    // run the model

    return {
      X_AXIS_LABEL: 'ACOX2 (Liver)',
      Y_AXIS_LABEL: 'KCNE4 (Heart)',
      PLOT_TYPE: 'scatter',
    };
  }
}
