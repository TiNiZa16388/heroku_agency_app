import { Component, OnInit, Input } from '@angular/core';
import { Actor, AgencyService } from 'src/app/services/agency.service';
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
    ) { }

  ngOnInit() {
    if (this.isNew) {
      this.actor = {
        id: -1,
        gender: '',
        age: -1,
        name: '',
        movies: []
      };
      this.addMovie();
    }
  }

  customTrackBy(index: number, obj: any): any {
    return index;
  }

  addMovie(i: number = 0) {
    this.actor.movies.splice(i + 1, 0, {title: ''});
  }

  removeMovie(i: number) {
    this.actor.movies.splice(i, 1);
  }

  closeModal() {
    this.modalCtrl.dismiss();
  }

  saveClicked() {
    this.agencyService.saveActor(this.actor);
    this.closeModal();
  }

  deleteClicked() {
    this.agencyService.deleteActor(this.actor);
    this.closeModal();
  }
}
