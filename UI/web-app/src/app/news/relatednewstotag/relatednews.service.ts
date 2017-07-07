import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Rx';


@Injectable()
export class RelatedNewsService {
    constructor(private http: Http) {
    }
    getRelatedNews(newsurl: string): Observable<any> {
        return this.http.get(newsurl);
    }
}
