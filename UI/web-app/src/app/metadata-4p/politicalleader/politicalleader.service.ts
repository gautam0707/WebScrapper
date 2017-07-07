import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';


@Injectable()
export class PoliticalLeaderService {
    private politicalleaderdetailsurl = 'http://localhost:8000/PoliticalLeader';
    constructor(private http: Http) {
    }
    getLeaderDetails(leaderId: string): Observable<any> {
        return this.http.get(this.politicalleaderdetailsurl + '/?leaderId=' + leaderId);
    }
}
