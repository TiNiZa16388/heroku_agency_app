import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { MoviePage } from './movie.page';
import { MovieFormComponent } from './movie-form/movie-form.component';

const routes: Routes = [
  {
    path: '',
    component: MoviePage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  entryComponents: [MovieFormComponent],
  declarations: [MoviePage, MovieFormComponent],
})
export class MoviePageModule {}
