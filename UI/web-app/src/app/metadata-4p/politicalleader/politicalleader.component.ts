import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PoliticalLeaderService } from './politicalleader.service';
@Component({
    selector: 'app-political-leader',
    templateUrl: 'politicalleader.component.html'
})
export class PoliticalLeaderComponent implements OnInit {
    private leaderInfo;
    constructor(private leaderservice: PoliticalLeaderService, private route: ActivatedRoute) {
    }
    getLeaderDetails(leaderId: string) {
        this.leaderservice.getLeaderDetails(leaderId).subscribe((response) => {
            this.leaderInfo = JSON.parse(response._body);
            console.log(this.leaderInfo);
        });
    }
    ngOnInit() {
        const leaderId: string = this.route.snapshot.params['id']
        this.getLeaderDetails(leaderId);
    }
}
