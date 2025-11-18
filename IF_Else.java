import java.util.*;
public class IF_Else{
    public static void main(String[] args){
        Scanner j = new Scanner(System.in);
        System.out.print("Enter the age: ");
        int age = j.nextInt();
        if(age >= 18){
            System.out.println("You are an adult");
        }
        else if(age >= 12 && age < 18){
            System.out.println("You are a Teenager");
        }
        else{
            System.out.println("You are a Child! Focus on Studies");
        }
    }
}
