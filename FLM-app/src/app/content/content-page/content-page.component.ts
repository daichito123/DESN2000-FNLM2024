import { Component } from '@angular/core';
import { QueryServiceService } from '../../query-service.service';



@Component({
  selector: 'app-content-page',
  templateUrl: './content-page.component.html',
  styleUrl: './content-page.component.scss'
})

export class ContentPageComponent {
  isExpanded = false;
  public queryService: QueryServiceService;
  constructor(queryService:QueryServiceService){
    this.queryService = queryService;
  }
  
  toggleWidth() {
    this.isExpanded = !this.isExpanded;
  }


}

