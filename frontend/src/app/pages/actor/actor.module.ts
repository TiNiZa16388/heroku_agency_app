import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { ActorPage } from './actor.page';
import { ActorFormComponent } from './actor-form/actor-form.component';

const routes: Routes = [
  {
    path: '',
    component: ActorPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  entryComponents: [ActorFormComponent],
  declarations: [ActorPage, ActorFormComponent],
})
export class ActorPageModule {}
