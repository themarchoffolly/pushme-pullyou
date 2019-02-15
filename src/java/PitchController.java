package com.gitpitch.controller;

public class PitchController extends Controller {

    @Inject
    public PitchController(GitManager gitManager) {
        this.gitManager = gitManager;
    }
}
