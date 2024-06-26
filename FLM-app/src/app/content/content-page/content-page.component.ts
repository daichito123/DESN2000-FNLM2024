import { Component } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';


@Component({
  selector: 'app-content-page',
  templateUrl: './content-page.component.html',
  styleUrl: './content-page.component.scss'
})
export class ContentPageComponent {
  // userForm = new FormGroup();
  query = new FormControl('');


  print() {
    console.log(this.query.value)
  }
}

