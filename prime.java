import java.util.Scanner;

public class prime {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int a =sc.nextInt();
		
		for (int i=2;i<a/2;++i)		{
			if (a%i==0)
			{
				System.out.print("Non Prime");
				break;
			}
		
		if (i>=a/2-1) {
			System.out.print("Prime");
		}
		}
		
	}
}
