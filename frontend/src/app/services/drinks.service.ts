import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

export interface Drink {
  id: number;
  title: string;
  recipe: Array<{
          name: string,
          color: string,
          parts: number
        }>;
}

export interface Movie {
  id: number;
  title: string;
  release_date: Date;
  actors: Array<{
    name: string
  }>
}

export interface Actor {
  id:number;
  name: string;
  gender: string;
  ag: number;
  movies: Array<{
    title: string
  }>
}

@Injectable({
  providedIn: 'root'
})
export class AgencyService {

  url = environment.apiServerUrl;

  public movies: {[key: number]: Movie} = {};
  public actors : {[key: number]: Actor} = {};

  constructor(private auth: AuthService, private http: HttpClient) { }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
      .set('Authorization', `Bearer ${this.auth.activeJWT()}`)
    };
    return header;
  }

  getActors() {
    if (this.auth.can('get:actors')) {
      this.http.get(this.url + '/actors', this.getHeaders())
      .subscribe((res: any) => {
        this.fillActors(res.actors)
        console.log(res)
      })
    }
  }

  saveActor(actor: Actor) {
    if (actor.id >= 0){
      this.http.patch(this.url + '/actors/' + actor.id, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.fillActors(res.actors)
        }
      });
    } else {
      this.http.post(this.url + '/actors', actor, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.fillActors(res.actors);
        }
      })
    }
  }

  deleteActor(actor: Actor){
    delete this.actors[actor.id];
    this.http.delete(this.url + '/actors/' + actor.id, this.getHeaders())
    .subscribe( (res:any) => {

    });
  }

  getMovies() {
    if (this.auth.can('get:movies')) {
      this.http.get(this.url + '/movies', this.getHeaders())
      .subscribe((res: any) => {
        this.fillMovies(res.movies)
        console.log(res)
      })
    }
  }

  saveMovie(movie: Movie) {
    if (movie.id >= 0){
      this.http.patch(this.url + '/movies/' + movie.id, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.fillMovies(res.movies)
        }
      });
    } else {
      this.http.post(this.url + '/movie/', movie.id, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.fillMovies(res.movies);
        }
      })
    }
  }

  deleteMovie(movie: Movie){
    delete this.movies[movie.id];
    this.http.delete(this.url + '/movies/' + movie.id, this.getHeaders())
    .subscribe( (res:any) => {

    });
  }

  fillActors( actors: Array<Actor>){
    for (const actor of actors) {
      this.actors[actor.id] = actor;
    }
  }

  fillMovies( movies: Array<Movie>){
    for (const movie of movies) {
      this.movies[movie.id] = movie;
    }
  }

}

@Injectable({
  providedIn: 'root'
})
export class DrinksService {

  url = environment.apiServerUrl;

  public items: {[key: number]: Drink} = {};

  constructor(private auth: AuthService, private http: HttpClient) { }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${this.auth.activeJWT()}`)
    };
    return header;
  }

  getDrinks() {
    if (this.auth.can('get:drinks-detail')) {
      this.http.get(this.url + '/drinks-detail', this.getHeaders())
      .subscribe((res: any) => {
        this.drinksToItems(res.drinks);
        console.log(res);
      });
    } else {
      this.http.get(this.url + '/drinks', this.getHeaders())
      .subscribe((res: any) => {
        this.drinksToItems(res.drinks);
        console.log(res);
      });
    }

  }

  saveDrink(drink: Drink) {
    if (drink.id >= 0) { // patch
      this.http.patch(this.url + '/drinks/' + drink.id, drink, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.drinksToItems(res.drinks);
        }
      });
    } else { // insert
      this.http.post(this.url + '/drinks', drink, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.drinksToItems(res.drinks);
        }
      });
    }

  }

  deleteDrink(drink: Drink) {
    delete this.items[drink.id];
    this.http.delete(this.url + '/drinks/' + drink.id, this.getHeaders())
    .subscribe( (res: any) => {

    });
  }

  drinksToItems( drinks: Array<Drink>) {
    for (const drink of drinks) {
      this.items[drink.id] = drink;
    }
  }

}
