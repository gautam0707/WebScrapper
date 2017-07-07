import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';


@Injectable()
export class ConstituencyService {
    private constituencydetailsurl = 'http://localhost:8000/Constituency';
    constructor(private http: Http){
    }
    getConstituencyDetails(constituencyId: string): Observable<any> {
        return this.http.get(this.constituencydetailsurl + '/?constituencyId=' + constituencyId);
    }
}
