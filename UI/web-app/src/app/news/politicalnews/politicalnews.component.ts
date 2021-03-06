import { Component, OnInit } from '@angular/core';
import { NewsService } from '../news.service';
@Component({
    selector: 'app-political-news',
    templateUrl: 'politicalnews.component.html'
})
export class PoliticalNewsComponent implements OnInit {
    private news: any[];
    private headings: string[];
    private newsItems: string[];
    private newsPresented: any[] = [];
    private newsurl = 'http://localhost:8000/PoliticalNews';
    private newsCount: number = 0;
    constructor(private newsService: NewsService) {
    }
    getNews() {
        this.newsService.getNews(this.newsurl).subscribe((news) => {
            this.news = JSON.parse(news._body);
            console.log(this.news);
            this.newsCount = this.news.length;
            if (!!this.news) {
                for (let j = 0; j < this.newsCount; j++) {
                    const temp = { heading: '', newsItem: '', imageurls: [] };
                    for (let i = 0; i < this.news[j].Headings.length; i++) {
                        temp.heading += this.news[j].Headings[i] + ' <br> ';
                    }
                    for (let i = 0; i < this.news[j].News.length; i++) {
                        temp.newsItem += this.news[j].News[i] + ' <br> ';
                    }
                    for (let i = 0; i < this.news[j].imageids.length; i++) {
                        temp.imageurls.push('http://localhost:8000/Image?imageId=' + this.news[j].imageids[i]);
                    }
                    this.newsPresented.push(temp);
                }
            }
        });
    }

    ngOnInit() {
        this.getNews();
    }
}
