import unittest
import prac 
from unittest.mock import patch
import sys
import io
from contextlib import redirect_stdout


class TestCases(unittest.TestCase):
    
    def  test_quick_maths(self):
        add = prac.quick_maths("one","one","+")
        multiply = prac.quick_maths("five","two","*")
        self.assertEqual(add,2)
        self.assertEqual(multiply,10)
        self.assertIsInstance(add,int)
        self.assertIsInstance(multiply,int)

    def  test_give_me_the_digits(self):
        my_list = prac.give_me_the_digits([1,"Team 17-18",3,"good_morning",7,"I'm trolling you !",9,3,7])
        my_list_two = prac.give_me_the_digits(["1","3",3,6,"20","slides","for","7",1,"presentation","!"])
        self.assertEqual(my_list,[2,6,14,18,6,14])
        self.assertEqual(my_list_two,[2,6,6,12,40,14,2])
        self.assertIsInstance(my_list_two,list) 
    
    # Note: one of the ways to capture stdout 
    
    def test_triangle_right_angle(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prac.fun_triangle(5)
        out =f.getvalue()    
        self.assertEqual(out,'1 \n2 4 \n3 6 9 \n4 8 12 16 \n5 10 15 20 25 \n')


    def test_triangle_right_angle_down(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prac.fun_triangle_upside_down(5)
        out =f.getvalue()    
        self.assertEqual(out,'1 2 3 4 5 \n2 4 6 8 \n3 6 9 \n4 8 \n5 \n') 


    def test_hill_pattern(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prac.im_a_hill_kinda(5)
        out =f.getvalue()    
        self.assertEqual(out,'1 \n2 4 \n3 6 9 \n4 8 12 16 \n5 10 15 20 25 \n1 2 3 4 5 \n2 4 6 8 \n3 6 9 \n4 8 \n5 \n')    
              
    def test_remove_duplicates(self):
        my_list = prac.remove_duplicates("961122233447733114477866674455538885499918882999")
        self.assertEqual(my_list,list(map(str,[1,2,3,4,5,6,7,8,9])))

    def test_fizzbuzz(self):
        case_one = prac.fizz_buzz(3)
        case_two = prac.fizz_buzz(5)
        case_three = prac.fizz_buzz(15)
        case_four = prac.fizz_buzz(2)
        self.assertEqual(case_one,"Fizz")
        self.assertEqual(case_two,"Buzz")
        self.assertEqual(case_three,"Fizzbuzz")
        self.assertEqual(case_four,"2")
        

    def test_validate(self):
        self.assertTrue(len(prac.read_me())==9)
        self.assertEqual(prac.read_me(),['Anna', 'is', 'a', 'palidrome', 'with', 'the', 'length', 'of', 'cool']) 
        self.assertEqual(prac.validate_string("Anna"),True)
        self.assertEqual(prac.validate_string("cool"),False)
        self.assertEqual(prac.simple_palidrome("Anna","Anna is a palidrome."))
        self.assertEqual(prac.simple_palidrome("four","four is not a palidrome."))  


          
        

        
        

