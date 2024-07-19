import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import {Component} from '@angular/core';
import { ContentPageComponent } from './content-page/content-page.component';
import { IntroStateComponent } from './intro-state/intro-state.component';
import { QueryStateComponent } from './query-state/query-state.component';

import {ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatButtonModule} from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import {MatIconModule} from '@angular/material/icon';




@NgModule({
  declarations: [ContentPageComponent, IntroStateComponent, QueryStateComponent],
  imports: [
    CommonModule,
    MatSidenavModule,
    MatButtonModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
  ],
  exports: [
    ContentPageComponent,
    IntroStateComponent,
    QueryStateComponent
  ]
})
export class ContentModule { }
