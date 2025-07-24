using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _4_集合
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //introduceList();
            //introduceBianLi();
            ExampleStaff();
            Console.ReadKey();
        }
        public static void introduceList()
        {
            #region 1维数组 数组长度不可变
            int[] list1=new int[10];
            list1[5]=10;
            Console.WriteLine(list1[5]);
            Console.WriteLine(list1[0]);

            string[] color = { "红", "橙", "黄", "绿", "青", "蓝", "紫" };
            Console.WriteLine(color[3]);
            Console.WriteLine(color.Length);
            //color[8] = "黑";//System.IndexOutOfRangeException:“索引超出了数组界限。”
            #endregion
            #region 多维数组
            //定义方式1
            int[,] list2=new int[2,2];
            list2[1, 1] = 88;
            Console.WriteLine("list2[1,1]={0},list2.length={1}", list2[1,1],list2.Length);
            //定义方式2
            int[,] list3 = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 } };
            Console.WriteLine("list3[0,0,]={0},list3.length={1}", list3[0,0],list3.Length);
            //定义方式3
            int[,] list4 = new int[2, 2] { { 1, 2 }, { 7, 8 } };
            Console.WriteLine(list4[0, 0]);

            string[,,] strList = {
                { { "1", "2", "3" }, { "2", "3", "4" }, { "3", "4", "5" } },//0
                { {"11","12","13" },{ "14","15","16"},{ "17","18","19"} } ,//1
                {{"100","200","300"},{ "400","500","600"},{ "700","800","900"} }};//2
            Console.WriteLine(strList[2,2,2]);//900 第一层索引为二的数组的索引为二的数组的索引为二的数字

            #endregion
            #region 交错数组
            int[][] array1=new int[3][];

            array1[0] = new int[3] { 1, 2, 3 };
            array1[1] = new int[2] { 4, 5 };
            array1[2] = new int[1] { 6 };
            //输出6
            Console.WriteLine(array1[2][0]);
            //可以直接在初始化的时候定义变量 类似Java
            int[][] array2 =
            {
                new int[]{1,2,3,4},
                new int[]{4,5,6,7 },
                new int[]{100,200,300 }
            };
            //与多维数组混用
            int[][,] array3 =
            {
                new int[,] { { 1,2},{ 3,4} },
            };
            Console.WriteLine(array3[0][0,0]);
            #endregion
            #region 隐式类型的数组
            int[] a = new[] { 1, 2, 3, 5, 6, 7, 8, 9 };
            string[,] b = new[,] { { "1", "2" }, { "3", "4" } };

            //推断类型
            var m = "你好！";
            var n = 36978106;
            var pi = 3.14f;
            #endregion
        }
        public static void introduceBianLi() 
        {
            #region 数组的遍历
            int[] list1 = new int[] { 1, 2, 3, 4, 5, 6 };
            for (int i = 0; i < list1.Length; i++)
            {
                Console.WriteLine(list1[i]);
            }
            Console.WriteLine();
            int[,] list2 = new int[,] { {1,2 }, { 3,4} };
            for (int i = 0;i < list2.GetLength(0); i++)
            {
                for (int j = 0; j < list2.GetLength(1); j++)
                {
                    Console.WriteLine(list2[i,j]);
                }
            }
            //foreach
            foreach (int item in list2)//(var item in list2)
            {
                Console.WriteLine(item);
            }
            #endregion
        }
        public static void ExampleStaff()
        {
            //用户进入系统后，输入1更改信息，输入2可查看所有员工信息输入3退出系统
            //公司一共3个工位，有编号分别是0 - 9，用户可以选择查看对应编号工位的员工信息、修改员工信息或退出程序
            //用户可以输入员工的姓名、年龄和薪水来更新对应工位员工信息。
            //用户可以选择要查看的工位编号，并显示相应员工的信息。
            //用户可以选择要修改的员工编号，并输入新的年龄和薪水来修改员工信息。
            //整个系统会一直循环运行，直到用户没有想要做的事情后，选择退出程序，程序才会结束运行。
            STAFF[] staffs = new STAFF[30];
            int count = 0;
            for (int i = 0; i < 3; i++)
            {
                for(int j = 0;j < 10; j++)
                {
                    staffs[count]=new STAFF();
                    staffs[count].POSITIONNUMBER = i;
                    staffs[count].STAFFNUMBER = j;
                    staffs[count].NAME = i.ToString()+j.ToString();
                    staffs[count].AGE = 25;
                    staffs[count].WAGES = 5000;
                    count++;
                }
            }
            
            while (true)
            {
                Console.WriteLine("欢迎进入员工信息系统！输入1更改信息，输入2可查看所有员工信息，输入3退出系统");
                Console.Write("您的输入：");
                try
                {
                    int input = int.Parse(Console.ReadLine());
                    if (input<1 || input>3)
                    {
                        continue;
                    }else if (input==1)
                    {
                        try
                        {
                            Console.Write("请输入员工工位号：");
                            int pos = int.Parse(Console.ReadLine());
                            Console.Write("请输入员工编号：");
                            int num = int.Parse(Console.ReadLine());
                            changeInfor(pos, num,staffs);
                        }
                        catch
                        {
                            Console.WriteLine("不正确的输入，请检查后重新输入！");
                            continue;
                        }
                    }else if (input==2)
                    {
                        foreach (var item in staffs)
                        {
                            item.showInfor();
                        }
                    }else if (input == 3)
                    {
                        Console.WriteLine("您已退出系统！");
                        break;
                    }
                }
                catch 
                {
                    Console.WriteLine("不正确的输入，请检查后重新输入！");
                    continue;
                }
            }

        }
        public static void changeInfor(int num1, int num2, STAFF[] a)
        {
            foreach (var item in a)
            {
                if (item.POSITIONNUMBER == num1 && item.STAFFNUMBER == num2)
                {
                    item.showInfor();
                    Console.Write("输入要更改的信息，不修改请输入“no”\n姓名：");
                    string name= Console.ReadLine();
                    if (name=="no")
                    {
                        break;
                    }
                    item.NAME=name;

                    try
                    {
                        Console.Write("年龄：");
                        item.AGE= int.Parse(Console.ReadLine());
                        Console.Write("工资：");
                        item.WAGES = float.Parse(Console.ReadLine());
                        Console.WriteLine("已更改！");
                        item.showInfor();
                        break;
                    }
                    catch 
                    { 
                        Console.WriteLine("不正确的输入，请检查后重新输入！"); 
                        break; 
                    }
                }
            }
        }
        public class STAFF
        {
            public int POSITIONNUMBER;
            public int STAFFNUMBER;
            public string NAME;
            public int AGE;
            public float WAGES;

            public void showInfor()
            {
                Console.WriteLine("工位{0}，编号{1}，姓名{2}，年龄{3}，薪水{4}",POSITIONNUMBER, STAFFNUMBER, NAME, AGE, WAGES);
            }
        }

    }
}
