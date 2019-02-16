package com.gitpitch.controller;

public class PitchController extends Controller {

    @Inject
    public PitchController(Object gitManager) {
        this.gitManager = gitManager;
    }
}
