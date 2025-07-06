import { Component, OnInit, Input } from '@angular/core';
import { Actor, Movie, AgencyService } from 'src/app/services/agency.service';
import { IonDatetime, ModalController } from '@ionic/angular';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-movie-form',
  templateUrl: './movie-form.component.html',
  styleUrls: ['./movie-form.component.scss'],
})
export class MovieFormComponent implements OnInit {
  @Input() movie: Movie;
  @Input() isNew: boolean;

  private actors: {[key: number]: Actor} = {};

  constructor(
    public auth: AuthService,
    private modalCtrl: ModalController,
    private agencyService: AgencyService
    ){}

  ngOnInit() {
    if (this.isNew) {
      this.movie = {
        id: -1,
        title: '',
        release_date: '',
        actors: []
      };
      this.movie.release_date=new Date().toISOString();
    }
    this.agencyService.getActors();
  }

  customTrackBy(index: number, obj: any): any {
    return index;
  }

  addActor(i: number = 0) {
    this.agencyService.getActors();
    this.movie.actors.splice(this.movie.actors.length + 1, 0, 
      {
        id: 0,
        name: '',
        gender: '',
        age: -1,
        movies: []
      });

  }

  removeActor(i: number) {
    this.movie.actors.splice(i, 1);
    this.agencyService.getMovies();
    this.agencyService.getActors();
  }

  closeModal() {
    this.modalCtrl.dismiss();
  }

  saveClicked() {
    this.agencyService.saveMovie(this.movie);
    this.agencyService.getActors();
    this.closeModal();
  }

  deleteClicked() {
    this.agencyService.deleteMovie(this.movie);
    this.agencyService.getActors();
    this.closeModal();
  }

  getKeys(dictionary: { [key: number]: Actor }): string[] {
    return Object.keys(dictionary);
  }

}
