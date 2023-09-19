package moom.math.exercises.controller;

import moom.math.exercises.service.EuclideanDivisionService;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller("e6")
public class EuclideanDivisionController {

    private EuclideanDivisionService service;

    @GetMapping("longDivisionAlgorithm")
    public String longDivisionAlgorithm() {
        return null;
    }

    @GetMapping("binaryRepresentation")
    public String binaryRepresentation() {
        return null;
    }

    public void setService(EuclideanDivisionService service) {
        this.service = service;
    }

}