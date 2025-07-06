import { Component, OnInit, Input } from '@angular/core';
import { Actor, Movie, AgencyService } from 'src/app/services/agency.service';
import { ModalController } from '@ionic/angular';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-actor-form',
  templateUrl: './actor-form.component.html',
  styleUrls: ['./actor-form.component.scss'],
})
export class ActorFormComponent implements OnInit {
  @Input() actor: Actor;
  @Input() isNew: boolean;

  constructor(
    public auth: AuthService,
    private modalCtrl: ModalController,
    private agencyService: AgencyService
    ){}

  ngOnInit() {
    console.log("Actor Form opened!");
    this.agencyService.getMovies();
    this.agencyService.getActors();
    if (this.isNew) {
      this.actor = {
        id: -1,
        gender: '',
        age: -1,
        name: '',
        movies: []
      };
    }else{
      this.refreshMovies();
      console.log(JSON.stringify(this.actor))
    }
  }

  refreshMovies(){

    console.log("Refreshing actor movies buffer");
    console.log("Length: " + JSON.stringify(this.actor.movies.length))
    // Get all associated attributes of a movie
    // title is also used in the form html
    for(let i:number=0; i<this.actor.movies.length; i++){
      console.log("Iterate: " + JSON.stringify(i))
      console.log("this.actor.movies[i]: " + JSON.stringify(this.actor.movies[i]))
      // Check if property id exists in element of array
      if(this.actor.movies[i].hasOwnProperty("id")){
        let key = this.actor.movies[i].id;
        console.log("key:" + JSON.stringify(key))
        // check if IDs are identical..
        if(key != -1){
          console.log("movie.id:" + JSON.stringify(this.actor.movies[i].id))
          console.log("agencyService.movies[key].id: " + 
            JSON.stringify(this.agencyService.movies[key].id))
          if (key === this.agencyService.movies[key].id){
            this.actor.movies[i]=this.agencyService.movies[key];
            console.log("movie.id:" + this.actor.movies[i].id);
            console.log("movie.release_date:" + this.actor.movies[i].release_date);
            console.log("movie.title:" + this.actor.movies[i].title);
          }
        }
      }else{
          console.log("Buffer does not have elements with property id..");
      }
    }
  }

  customTrackBy(index: number, obj: any): any {
    return index;
  }

  addMovie(i: number = 0) {
    this.agencyService.getMovies();
    this.actor.movies.push({
        id: -1,
        title: '',
        release_date: '',
        actors: []
      });
  }

  removeMovie(i: number) {
    this.actor.movies.splice(i, 1);
  }

  closeModal() {
    this.modalCtrl.dismiss();
  }

  saveClicked() {
    this.agencyService.saveActor(this.actor);
    this.agencyService.getMovies();
    this.agencyService.getActors();
    this.closeModal();
  }

  deleteClicked() {
    this.agencyService.deleteActor(this.actor);
    this.agencyService.getMovies();
    this.agencyService.getActors();
    this.closeModal();
  }

  getKeys(dictionary: { [key: number]: Object }): string[] {
    return Object.keys(dictionary);
  }

  handleChange(event: Event) {
    const target = event.target as HTMLIonSelectElement;

    console.log("Handle Change called!")
    console.log("Target:" + JSON.stringify(target))

    this.refreshMovies();

  }

}
