import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import {Observable} from 'rxjs/Rx';


@Injectable()
export class NewsService {
    constructor(private http: Http) {
    }
    getNews(newsurl: string): Observable<any> {
        return this.http.get(newsurl);
    }
}
