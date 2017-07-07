import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ElectionYearService } from './electionyear.service';
@Component({
    selector: 'app-election-year',
    templateUrl: 'electionyear.component.html'
})
export class ElectionYearComponent implements OnInit{
    private electionYearInfo;
    constructor(private leaderservice: ElectionYearService, private route: ActivatedRoute) {
    }
    getElectionYearDetails(electionYearId: string) {
        this.leaderservice.getElectionYearDetails(electionYearId).subscribe((response) => {
            this.electionYearInfo = JSON.parse(response._body);
            console.log(this.electionYearInfo);
        });
    }
    ngOnInit() {
        const electionYearId: string = this.route.snapshot.params['id']
        this.getElectionYearDetails(electionYearId);
    }
}
