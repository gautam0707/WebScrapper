import { Routes } from '@angular/router';
import { PoliticalPartyComponent } from './app/metadata-4p/politicalparty/politicalparty.component';
import { NewsComponent } from './app/news/news.component';
import { NationalNewsComponent } from './app/news/nationalnews/nationalnews.component';
import { InternationalNewsComponent } from './app/news/internationalnews/internationalnews.component';
import { FinancialNewsComponent } from './app/news/financialnews/financialnews.component';
import { PoliticalNewsComponent } from './app/news/politicalnews/politicalnews.component';
import { PoliticalLeaderComponent } from './app/metadata-4p/politicalleader/politicalleader.component';
import { ElectionYearComponent } from './app/metadata-4p/electionyear/electionyear.component';
import { ConstituencyComponent } from './app/metadata-4p/constituency/constituency.component';

export const appRoutes = [
    {
        path: 'PoliticalParty/:id',
        component: PoliticalPartyComponent
    },
    {
        path: 'PoliticalLeader/:id',
        component: PoliticalLeaderComponent
    },
    {
        path: 'ElectionYear/:id',
        component: ElectionYearComponent
    },
    {
        path: 'Constituency',
        component: ConstituencyComponent
    },
    {
        path: 'News',
        component: NewsComponent
    },
    {
        path: 'PoliticalNews',
        component: PoliticalNewsComponent
    },
    {
        path: 'FinancialNews',
        component: FinancialNewsComponent
    },
    {
        path: 'NationalNews',
        component: NationalNewsComponent
    },
    {
        path: 'InternationalNews',
        component: InternationalNewsComponent
    },
    {
        path: '',
        redirectTo: 'News',
        pathMatch: 'full'
    }
];
