using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _6_案例
{
// 题目：
//设计一个角色任务系统，包含三种不同类型的任务：消灭怪物、收集物品和护送NPC。每种任务都有特定的要求和奖励。
//要求：
//定义一个基类Task，包含任务的共有属性和方法，如任务名称（name）、任务描述（description）和任务奖励金币(reward）。
//定义至少三个派生类（子类），分别表示消灭怪物任务（KillMonsterTask）、收集物品任务（CollectltemTask）和护送NPC任务（EscortNPCTask）。
//使用构造函数来初始化任务对象，并展示基类的初始化过程，三个任务放在同一个数组里进行统一管理。
//使用成员函数来描述任务的行为，如开始任务、完成任务等。
//使用封装来保护任务的特定成员（monsterCount，item，npc），并展示不同访问修饰符的作用。
//每个子类应该重写基类的方法，实现各自的特定功能。
//使用静态成员来表示任务的数量，并实现统计功能。完成一个任务，数量+1，达到3游戏结束，有一个bool值doingTask来检测当前的任务执行状态
//按下S键开始当前任务，按下C完成当前任务
//使用this和base关键字来引引用当前对象和基类对象。
//使用重写、阻止重写和隐藏基类成员来展示多态性的不同表现形式。
    internal class Program
    {
        static void Main(string[] args)
        {
            Task[] tasks =
                {
                new KillMonsterTask("临危受命","消灭盘踞的丘丘人",10,8),
                new EscortNPCTask("苦恼的爱莲博士","护送爱莲博士前往纳塔",160,"爱莲"),
                new CollectltemTask("一个奇怪的……","收集10个新鲜的落落莓",10, 10)
            };
            Console.WriteLine("欢迎玩元神，s开始任务，c结束任务");
            while (Task.taskNum<3)
            {
                string s=Console.ReadLine();
                if (s == "s")
                {
                    if (!Task.doingTask)
                    {
                        Task.doingTask = true;
                        tasks[Task.taskNum].StartTask();
                    }

                }
                else if (s =="c")
                {
                    if (Task.doingTask) 
                    {
                        Task.doingTask= false;
                        tasks[Task.taskNum].EndTask();
                        Task.taskNum++;
                    }
                }
            }
            Console.WriteLine("GAME OVER");

            Console.ReadKey();
        }

        class Task
        {
            public string name;
            public string description;
            public int reward;
            public static bool doingTask;

            public static int taskNum;

            public Task(string name, string description, int reward)
            {
                this.name = name;
                this.description = description;
                this.reward = reward;
            }

            public virtual void StartTask()
            {
                Console.WriteLine("开始任务：" + name);
            }
            public virtual void EndTask()
            {
                Console.WriteLine("完成"+name+"，获得"+reward+"原石奖励");
            }
        }
        class KillMonsterTask : Task
        {
            private int monsterCount;
            public KillMonsterTask(string name, string description, int reward, int monsterCount) : base(name, description, reward)
            {
                this.monsterCount = monsterCount;
            }
            public override void StartTask()
            {
                base.StartTask();
                Console.WriteLine("需要消灭"+monsterCount+"只丘丘人");
            }
            public override void EndTask()
            {
                base.EndTask();
            }
        }
        class CollectltemTask : Task
        {
            private int item;
            public CollectltemTask(string name, string description, int reward,int item) : base(name, description, reward)
            {
                this.item = item;
            }
            public override void StartTask()
            {
                base.StartTask();
                Console.WriteLine("需要收集" + item + "个物品");
            }
        }

        class EscortNPCTask : Task
        {
            private string NPC;
            public EscortNPCTask(string name, string description, int reward,string npc) : base(name, description, reward)
            {
                this.NPC = npc;
            }
            public override void StartTask() 
            { 
                base .StartTask();
                Console.WriteLine("需要护送" + NPC);
            }
        }
    }
}
