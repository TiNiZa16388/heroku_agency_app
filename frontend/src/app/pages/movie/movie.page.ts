import { Component, OnInit } from '@angular/core';
import { AgencyService, Movie } from '../../services/agency.service';
import { ModalController } from '@ionic/angular';
import { MovieFormComponent } from './movie-form/movie-form.component';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-movie',
  templateUrl: './movie.page.html',
  styleUrls: ['./movie.page.scss'],
})
export class MoviePage implements OnInit {
  Object = Object;

  constructor(
    private auth: AuthService,
    private modalCtrl: ModalController,
    public agency: AgencyService
    ) { }

  ngOnInit() {
    this.agency.getMovies();
  }

  async openForm(activeMovie: Movie = null) {


    const modal = await this.modalCtrl.create({
      component: MovieFormComponent,
      componentProps: { movie: activeMovie, isNew: !activeMovie , AgencyService: this.agency}
    });

    modal.present();
  }

}
