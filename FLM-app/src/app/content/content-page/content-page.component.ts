import { Component } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import { ChartData, ChartOptions } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';
import Chart from 'chart.js/auto';


@Component({
  selector: 'app-content-page',
  templateUrl: './content-page.component.html',
  styleUrl: './content-page.component.scss'
})

export class ContentPageComponent {
  public chart: any;

  ngOnInit(): void {
    this.createChart();
  }

  query = new FormControl('');

  print() {
    console.log(this.query.value)
  }

  createChart(){
    this.chart = new Chart("MyChart", {
      type: 'bar', //this denotes tha type of chart

      data: {// values on X-Axis
        labels: ['Cell 1', 'Cell 2', 'Cell 3','Cell 4',
								 'Cell 5', 'Cell 6', 'Cell 7','Cell 8', ], 
	       datasets: [
          {
            label: "Gene 1",
            data: ['467','576', '572', '79', '92',
								 '574', '573', '576'],
            backgroundColor: 'blue'
          },
          {
            label: "Gene 2",
            data: ['542', '542', '536', '327', '17',
									 '0.00', '538', '541'],
            backgroundColor: 'limegreen'
          }  
        ]
      },
      options: {
        aspectRatio:2.5
      }
      
    });
  }
}

