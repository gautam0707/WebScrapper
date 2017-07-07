import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.root.component';
import { PoliticalPartyService } from './metadata-4p/politicalparty/politicalparty.service';
import { NewsService } from './news/news.service';

import { RouterModule } from '@angular/router';
import { appRoutes } from '../routes';
import { PoliticalPartyComponent } from './metadata-4p/politicalparty/politicalparty.component';
import { NewsComponent } from './news/news.component';
import { NationalNewsComponent } from './news/nationalnews/nationalnews.component';
import { InternationalNewsComponent } from './news/internationalnews/internationalnews.component';
import { FinancialNewsComponent } from './news/financialnews/financialnews.component';
import { PoliticalNewsComponent } from './news/politicalnews/politicalnews.component';
import { PoliticalLeaderComponent } from './metadata-4p/politicalleader/politicalleader.component';
import { ElectionYearComponent } from './metadata-4p/electionyear/electionyear.component';
import { ConstituencyComponent } from './metadata-4p/constituency/constituency.component';

import { ConstituencyService } from './metadata-4p/constituency/constituency.service';
import { PoliticalLeaderService } from './metadata-4p/politicalleader/politicalleader.service';
import { ElectionYearService } from './metadata-4p/electionyear/electionyear.service';
import { RelatedNewsComponent } from './news/relatednewstotag/relatednews.component';
import { RelatedNewsService } from './news/relatednewstotag/relatednews.service';

@NgModule({
  declarations: [
    AppComponent,
    PoliticalPartyComponent,
    NewsComponent,
    NationalNewsComponent,
    InternationalNewsComponent,
    FinancialNewsComponent,
    PoliticalNewsComponent,
    PoliticalLeaderComponent,
    ElectionYearComponent,
    ConstituencyComponent,
    RelatedNewsComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [
    PoliticalPartyService,
    ConstituencyService,
    ElectionYearService,
    PoliticalLeaderService,
    NewsService,
    RelatedNewsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
