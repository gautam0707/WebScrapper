import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';


@Injectable()
export class PoliticalPartyService {
    private politicalpartydetailsurl = 'http://localhost:8000/PoliticalParty';
    constructor(private http: Http) {
    }
    getPartyDetails(partyId: string): Observable<any> {
        return this.http.get(this.politicalpartydetailsurl + '/?partyId=' + partyId);
    }
}
