import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContentPageComponent } from './content-page/content-page.component';
import {ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {FormsModule} from '@angular/forms';
import {MatButtonModule} from '@angular/material/button';
import { BaseChartDirective } from 'ng2-charts';

@NgModule({
  declarations: [ContentPageComponent],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule, 
    MatFormFieldModule, 
    MatInputModule,
    MatButtonModule,
    BaseChartDirective
  ],
  exports: [
    ContentPageComponent
  ]
})
export class ContentModule { }
