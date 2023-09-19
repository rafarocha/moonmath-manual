package moom.math.service;

import moom.math.exercises.service.EuclideanDivisionService;
import moom.math.exercises.service.SolutionLongDivision;
import org.junit.Test;
import org.junit.jupiter.api.Assertions;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.event.annotation.BeforeTestClass;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class EuclidianDivisionServiceTest {

    @Autowired
    private EuclideanDivisionService service;

    @Test public void longDivisionSimpleSucess() {
        long dividend = 143785, divisor = 17;
        SolutionLongDivision solution = service.longDivision(dividend, divisor);
        Assertions.assertEquals(8457, solution.quotient(), "quotient should be 8457");
        Assertions.assertEquals(16, solution.remainder(), "remainder should be 16");
    }

}