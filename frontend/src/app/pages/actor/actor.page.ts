import { Component, OnInit } from '@angular/core';
import { AgencyService, Actor } from '../../services/agency.service';
import { ModalController } from '@ionic/angular';
import { ActorFormComponent } from './actor-form/actor-form.component';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-actor',
  templateUrl: './actor.page.html',
  styleUrls: ['./actor.page.scss'],
})
export class ActorPage implements OnInit {
  Object = Object;

  constructor(
    private auth: AuthService,
    private modalCtrl: ModalController,
    public agency: AgencyService
    ) { }

  ngOnInit() {
    this.agency.getActors();
  }

  async openForm(activeActor: Actor = null) {

    console.log('Opening Actor Form Page')
    console.log(JSON.stringify(activeActor))

    const modal = await this.modalCtrl.create({
      component: ActorFormComponent,
      componentProps: { actor: activeActor, isNew: !activeActor , AgencyService: this.agency}
    });

    modal.present();
  }

}
