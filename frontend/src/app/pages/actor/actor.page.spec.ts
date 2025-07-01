import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ActorPage } from './actor.page';

describe('ActorPage', () => {
  let component: ActorPage;
  let fixture: ComponentFixture<ActorPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ActorPage ],
      schemas: [CUSTOM_ELEMENTS_SCHEMA],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ActorPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
