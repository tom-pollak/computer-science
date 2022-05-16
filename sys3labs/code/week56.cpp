#include <stdio.h>
#include <unistd.h>
#include <string.h>

#include "pipeline.hpp"

/////////////////////////////////////////////
// declare function prototypes

/////////////////////////////////////////////
// global variables and class instances

PipelineClass Pipe;

void ResolveHazards()
{
    Pipe.CalculateCycles();
    for (int i = 0; i < MAXSTAGES; i++)
    {
        for (int c = 0; c < Pipe.PipelinedCycles; c++)
        {
            if (Pipe.IsStageWB(i, c))
            {
            }
        }
    }
}

void ResolveSingleIssueHazards56a()
{
    Pipe.InsertStall(1, 3);
    Pipe.InsertStall(1, 3);

    Pipe.InsertStall(2, 4);
    Pipe.InsertStall(2, 4);
    Pipe.InsertStall(2, 4);

    Pipe.InsertStall(3, 2);
    Pipe.InsertStall(3, 4);
    Pipe.InsertStall(3, 4);
    Pipe.InsertStall(3, 4);
    Pipe.InsertStall(3, 4);
    Pipe.InsertStall(3, 4);

    Pipe.InsertStall(4, 6);

    Pipe.InsertStall(4, 7);
    Pipe.InsertStall(4, 7);
    Pipe.InsertStall(4, 7);
    Pipe.InsertStall(4, 7);
    Pipe.InsertStall(4, 7);
    Pipe.InsertStall(4, 7);
    Pipe.InsertStall(4, 7);
    Pipe.InsertStall(4, 7);
}

void ResolveSingleIssueHazards56b()
{
    Pipe.InsertStall(1, 3);
    Pipe.InsertStall(1, 3);

    Pipe.InsertStall(2, 3);
    Pipe.InsertStall(2, 3);
    Pipe.InsertStall(2, 3);
    Pipe.InsertStall(2, 3);
    Pipe.InsertStall(2, 3);

    Pipe.InsertStall(3, 7);

    Pipe.InsertStall(4, 5);
    Pipe.InsertStall(4, 5);
    Pipe.InsertStall(4, 5);

    Pipe.InsertStall(5, 9);
    Pipe.InsertStall(5, 9);

    Pipe.InsertStall(6, 7);

    Pipe.InsertStall(6, 8);
    Pipe.InsertStall(6, 8);
    Pipe.InsertStall(6, 8);
}

void ResolveSingleIssue56c()
{
    Pipe.InsertStall(1, 3);

    Pipe.InsertStall(2, 3);
    Pipe.InsertStall(2, 3);
    Pipe.InsertStall(2, 3);

    Pipe.InsertStall(0, 2);
    Pipe.InsertStall(0, 2);
    Pipe.InsertStall(0, 2);
    Pipe.InsertStall(0, 2);
    Pipe.InsertStall(0, 2);
    Pipe.InsertStall(0, 2);
    Pipe.InsertStall(0, 2);
}

//////////////////////////////////////////////

int main(int argc, char *argv[])
{
    int c = 0;

    printf("-- WEEK56.cpp --\n\n");
    Pipe.StartupMessage();

    // configure CPU settings

    if (1) // single issue
    {
        Pipe.IssueWidth = 1;
        Pipe.ReadPorts = 3;
        Pipe.WritePorts = 1;
        Pipe.IALUCount = 3;
        Pipe.FPALUCount = 1;
        Pipe.SHALUCount = 1;
        Pipe.CacheMode = 0;
    }
    else // superscalar 4
    {
        Pipe.IssueWidth = 4;
        Pipe.ReadPorts = 9;
        Pipe.WritePorts = 3;
        Pipe.IALUCount = 4;
        Pipe.FPALUCount = 1;
        Pipe.SHALUCount = 1;
        Pipe.CacheMode = 0;
    }

    // load in test case and show buffer

    c = Pipe.ReadAssemblerCode(argv[1]);
    if (c < 0)
    {
        return -1;
    }

    Pipe.DumpCodeList();

    // generate initial pipeline without and constraints

    Pipe.InitialSchedule();

    // output resulting pipeline diagram, and test for hazards
    Pipe.DumpPipeline();
    Pipe.PipelineTest();

    // perform hazard fixes
    //
    // calls to custom functions here

    // RAW Hazard ? --  RR.3(i2,c4)) WB.3,(i1,c8)

    // ResolveSingleIssueHazards56a();
    // ResolveSingleIssueHazards56b();

    // output resulting pipeline diagram, and test for hazards
    Pipe.DumpPipeline();
    Pipe.PipelineTest();

    // end of code
}
