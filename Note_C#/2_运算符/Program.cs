using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2_运算符
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //introduceMark();
            //GuessNumber();

            //introduceSwitch();
            //introduceDoAndWhile();
            Console.ReadKey();
        }
        public static void introduceMark()
        {
            #region
            //一元加，减
            Console.WriteLine(+5.4f);
            Console.WriteLine(-3);

            //增量运算符 谁在前前面就先继承谁
            int a = 5;
            Console.WriteLine("增量运算符");
            Console.WriteLine(a++);//后缀增加运算符 先输出 a 再计算
            Console.WriteLine(a);
            Console.WriteLine(++a);//前缀 先计算 a 再输出

            //减量运算符
            Console.WriteLine("减量运算符");
            Console.WriteLine(a--);
            Console.WriteLine(a);
            Console.WriteLine(--a);

            //二元运算符 加减乘除
            Console.WriteLine("加减乘除");
            float b = 1.1f;
            float c = 4.4f;
            Console.WriteLine(c + b);
            Console.WriteLine(c - b);
            Console.WriteLine(c * b);
            Console.WriteLine(c / b);

            #endregion
        }
        public static void GuessNumber()
        {
            int choice = 3;
            Console.WriteLine("你好，欢迎来到猜数游戏，你有{0}次机会猜1-9中的一个数字！",choice);
            Random ran = new Random();
            int n = ran.Next(1,10);
            
            for (int i = 0; i < choice; i++)
            {
                Console.Write("请输入您猜的数字：");
                try
                {
                    int yourNum = int.Parse(Console.ReadLine());//可能存在bug
                    if (yourNum == n)
                    {
                        Console.WriteLine("恭喜您，猜对了！");
                        break;
                    }
                    else if (yourNum > n)
                    {
                        if (i == choice-1)
                        {
                            Console.WriteLine("对不起，您没有机会了！");
                            break;
                        }
                        Console.WriteLine("很遗憾，您猜的数字大了！您还有{0}次机会！",(choice-1-i));
                    }
                    else
                    {
                        if (i == choice-1)
                        {
                            Console.WriteLine("对不起，您没有机会了！");
                            break;
                        }
                        Console.WriteLine("很遗憾，您猜的数字小了！您还有{0}次机会！",(choice-1-i));
                    }
                }
                catch (Exception e)
                {
                    if (i == choice - 1)
                    {
                        Console.WriteLine("对不起，您没有机会了！");
                        break;
                    }
                    Console.WriteLine("不正确的输入，损失一次机会！您还有{0}次机会！", (choice-1 - i));
                    continue;
                }                           
            }
            Console.WriteLine("这个数字是{0}！", n);

        }

        public static void introduceSwitch()
        {
            #region
            ROLE PLAYER = ROLE.MAGE;
            int HP = 0;
            int MP = 0;
            switch (PLAYER)
            {
                case ROLE.MAGE:
                    Console.WriteLine("The player is mage!");
                    HP = 60;
                    MP = 100;
                    break;
                case ROLE.WARRIOR:
                    Console.WriteLine("The player is warrior!");
                    HP = 100;
                    MP = 60;
                    break;
                case ROLE.ASSASSIN:
                    HP = 80;
                    MP = 80;
                    Console.WriteLine("The player is assassin!");
                    break;
                default:
                    Console.WriteLine("The player's role is unknown!");
                    break;
            }
            Console.WriteLine("The player is {0},this role's HP is {1},MP is {2}",PLAYER,HP,MP);
            


            #endregion
        }
        enum ROLE{
            MAGE,//法师
            WARRIOR,//战士
            ASSASSIN,//刺客
        }

        public static void introduceDoAndWhile()
        {
            int x = 0;
            do
            {
                Console.Write(x++);
            }
            while (x<5);

            Console.WriteLine("\n"+x+" not in loop!");
            while (x<10)
            {
                Console.Write(++x);
            }
        }
    }
}
