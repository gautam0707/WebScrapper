import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ConstituencyService } from './constituency.service';
@Component({
    selector: 'app-constituency',
    templateUrl: 'constituency.component.html'
})
export class ConstituencyComponent implements OnInit{
    private constituencyInfo;
    constructor(private leaderservice: ConstituencyService, private route: ActivatedRoute) {
    }
    getElectionYearDetails(constituencyId: string) {
        this.leaderservice.getConstituencyDetails(constituencyId).subscribe((response) => {
            this.constituencyInfo = JSON.parse(response._body);
            console.log(this.constituencyInfo);
        });
    }
    ngOnInit() {
        const constituencyId: string = this.route.snapshot.params['id']
        this.getElectionYearDetails(constituencyId);
    }
}
