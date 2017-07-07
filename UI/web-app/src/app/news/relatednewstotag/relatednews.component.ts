import { Component, OnInit, Input } from '@angular/core';
import { RelatedNewsService } from './relatednews.service';

@Component({
    selector: 'app-related-news-item',
    templateUrl: 'relatednews.component.html'
})
export class RelatedNewsComponent implements OnInit {
    @Input()
    private tagId;
    private news: any[];
    private headings: string[];
    private newsItems: string[];
    private newsPresented: any[] = [];
    private newsCount: number = 0;
    private newsurl = 'http://localhost:8000/RelatedNews';
    constructor(private newsService: RelatedNewsService) {
    }
    getNews() {
        this.newsurl += '?tagId='+this.tagId;
        this.newsService.getRelatedNews(this.newsurl).subscribe((news) => {
            this.news = JSON.parse(news._body);
            console.log(this.news);
            if (!!this.news) {
                this.newsCount = this.news.length;
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
