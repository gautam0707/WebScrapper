import { Component, OnInit } from '@angular/core';
import { PoliticalPartyService } from './politicalparty.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-political-party',
  templateUrl: 'politicalparty.component.html'
})
export class PoliticalPartyComponent implements OnInit {
  private partyInfo;
  constructor(private ppartyservice: PoliticalPartyService, private route: ActivatedRoute) {
  }
  getPartyDetails(partyId: string) {
    this.ppartyservice.getPartyDetails(partyId).subscribe((response) => {
      this.partyInfo = JSON.parse(response._body);
      console.log(this.partyInfo);
    });
  }
  ngOnInit() {
    const partyId: string = this.route.snapshot.params['id']
    this.getPartyDetails(partyId);
  }
}
