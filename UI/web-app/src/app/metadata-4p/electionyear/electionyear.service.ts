import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';


@Injectable()
export class ElectionYearService {
    private electionyeardetailsurl = 'http://localhost:8000/ElectionYear';
    constructor(private http: Http) {
    }
    getElectionYearDetails(electionYearId: string): Observable<any> {
        return this.http.get(this.electionyeardetailsurl + '/?electionYearId=' + electionYearId);
    }
}
