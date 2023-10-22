import java.io.*;
class IO {
public static void main(String args[])
throws IOException
{
FileInputStream fin
= new FileInputStream("oops.txt");
System.out.println(fin.getChannel());
System.out.println(fin.getFD());
try{
FileOutputStream fout=new FileOutputStream("oops.txt");
String s="welcome to javaTpoint.";
byte b[]=s.getBytes();//converting string into byte array
fout.write(b);
fout.close();
System.out.println("success...");
}catch(Exception e){System.out.println(e);}
System.out.println("FileContents :");
int ch;
while ((ch = fin.read()) != -1)
System.out.print((char)ch);
fin.close();
}
}