package com.gitpitch.controller;

public class PitchController extends Controller {

    @Inject
    public PitchController(Service gitManager) {
        this.gitManager = gitManager;
    }
}
