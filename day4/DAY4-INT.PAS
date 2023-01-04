{************************************************}
{                                                }
{  GENUARY 2023 - DAY 4 PROMPT - Intersections   }
{                                                }
{************************************************}

program Day4;

{
  This program is a demonstration of the Borland Graphics Interface (BGI)

  Runtime Commands for ARTY
  -------------------------
  <B>   - changes background color
  <C>   - changes drawcolor
  <ESC> - exits program
  Any other key pauses, then regenerates the drawing

  Note: If a /H command-line parameter is specified, the highest
        resolution mode will be used (if possible).
}

uses
  Crt, Graph;

const
   Memory  = 100;
   Windows =   4;

type
  ResolutionPreference = (Lower, Higher);
  ColorList = array [1..Windows] of integer;

var
  Xmax,
  Ymax,
  ViewXmax,
  ViewYmax : integer;

  Line:  array [1..Memory] of record
                                LX1,LY1: integer;
                                LX2,LY2: integer;
                                LColor : ColorList;
                              end;
  X1,X2,Y1,Y2,
  CurrentLine,
  ColorCount,
  IncrementCount,
  DeltaX1,DeltaY1,DeltaX2,DeltaY2: integer;
  Colors: ColorList;
  Ch: char;
  BackColor:integer;
  GraphDriver, GraphMode : integer;
  MaxColors : word;
  MaxDelta : integer;
  ChangeColors: Boolean;

procedure Frame;
begin
  SetViewPort(0, 0, Xmax, Ymax-(TextHeight('M')+4)-1,ClipOn);
  SetColor(MaxColors);
  Rectangle(0, 0, Xmax-1, (Ymax-(TextHeight('M')+4)-1)-1);
  SetViewPort(1, 1, Xmax-2, (Ymax-(TextHeight('M')+4)-1)-2,ClipOn);
end  { Frame };

procedure FullPort;
{ Set the view port to the entire screen }
begin
  SetViewPort(0, 0, Xmax, Ymax, ClipOn);
end; { FullPort }

procedure MessageFrame(Msg:string);
begin
  FullPort;
  SetColor(MaxColors);
  SetTextStyle(DefaultFont, HorizDir, 1);
  SetTextJustify(CenterText, TopText);
  SetLineStyle(SolidLn, 0, NormWidth);
  SetFillStyle(EmptyFill, 0);
  Bar(0, Ymax-(TextHeight('M')+4), Xmax, Ymax);
  Rectangle(0, Ymax-(TextHeight('M')+4), Xmax, Ymax);
  OutTextXY(Xmax div 2, Ymax-(TextHeight('M')+2), Msg);
  { Go back to the main window }
  Frame;
end  { MessageFrame };

procedure WaitToGo;
var
  Ch : char;
begin
{  MessageFrame('Press any key to continue... Esc aborts'); }
  repeat until KeyPressed;
  Ch := ReadKey;
  if Ch = #27 then begin
      CloseGraph;
      Writeln('All done.');
      Halt(1);
    end
  else
    ClearViewPort;
  { MessageFrame('Press a key to stop action, Esc quits.'); }
end; { WaitToGo }

procedure TestGraphError(GraphErr: integer);
begin
  if GraphErr <> grOk then begin
    Writeln('Graphics error: ', GraphErrorMsg(GraphErr));
    repeat until keypressed;
    ch := readkey;
    Halt(1);
  end;
end;

procedure Init;
var
  Err, I: integer;
  StartX, StartY: integer;
  Resolution: ResolutionPreference;
  s: string;
begin
  Resolution := Lower;
  if paramcount > 0 then begin
    s := paramstr(1);
    if s[1] = '/' then
      if upcase(s[2]) = 'H' then
        Resolution := Higher;
  end;

  CurrentLine    := 1;
  ColorCount     := 0;
  IncrementCount := 0;
  Ch := ' ';
  GraphDriver := Detect;
  DetectGraph(GraphDriver, GraphMode);
  TestGraphError(GraphResult);
  case GraphDriver of
    CGA        : begin
                   MaxDelta := 7;
                   GraphDriver := CGA;
                   GraphMode := CGAC1;
                 end;

    MCGA       : begin
                   MaxDelta := 7;
                   case GraphMode of
                     MCGAMed, MCGAHi: GraphMode := MCGAC1;
                   end;
                 end;

    EGA         : begin
                    MaxDelta := 16;
                    If Resolution = Lower then
                      GraphMode := EGALo
                    else
                      GraphMode := EGAHi;
                  end;

    EGA64       : begin
                    MaxDelta := 16;
                    If Resolution = Lower then
                      GraphMode := EGA64Lo
                    else
                      GraphMode := EGA64Hi;
                  end;

     HercMono   : MaxDelta := 16;
     EGAMono    : MaxDelta := 16;
     PC3270     : begin
                   MaxDelta := 7;
                   GraphDriver := CGA;
                   GraphMode := CGAC1;
                 end;


     ATT400     : case GraphMode of
                    ATT400C1,
                    ATT400C2,
                    ATT400Med,
                    ATT400Hi  :
                      begin
                        MaxDelta := 7;
                        GraphMode := ATT400C1;
                      end;
                  end;

     VGA         : begin
                     MaxDelta := 16;
                   end;
  end;
  InitGraph(GraphDriver, GraphMode, 'C:\TPWDB\BGI');
  TestGraphError(GraphResult);
  SetTextStyle(DefaultFont, HorizDir, 1);
  SetTextJustify(CenterText, TopText);

  MaxColors := GetMaxColor;
  BackColor := 0;
  ChangeColors := TRUE;
  Xmax := GetMaxX;
  Ymax := GetMaxY;
  ViewXmax := Xmax-2;
  ViewYmax := (Ymax-(TextHeight('M')+4)-1)-2;
  StartX := Xmax div 2;
  StartY := Ymax div 2;
  for I := 1 to Memory do with Line[I] do begin
      LX1 := StartX; LX2 := StartX;
      LY1 := StartY; LY2 := StartY;
    end;

   X1 := StartX;
   X2 := StartX;
   Y1 := StartY;
   Y2 := StartY;
end; {init}

procedure Rect(x1,y1,x2,y2:integer; Color:word);
var x:integer;
begin
  for x:=x1 to x2 do
  begin
    SetColor(color);
    Graph.Line(x,y1,x,y2);
  end;
end;

procedure RandBarPlay;
{ Draw random bars on the screen }
const
  W=150;
var
  MaxWidth  : integer;
  MaxHeight : integer;
  ViewInfo  : ViewPortType;
  Color     : word;
  i: integer;
  x1,y1:integer;
begin
  WaitToGo;
  i:=0;
  SetWriteMode(XORPUT);
  repeat
    Color := Random(GetMaxColor)+1;
{    SetFillStyle(SolidFill, Color); }
    x1:=Random(GetMaxX+W);
    y1:=Random(GetMaxY+W);
    Rect(x1-W,y1-W,x1+Random(W),y1+Random(W),Color);
    i := i+1;
  until (i=65);
  setWriteMode(COPYPUT);
  WaitToGo;
end; { RandBarPlay }

procedure WelcomeScreen;
begin
    SetTextJustify(CenterText, TopText);
    SetUserCharSize(5, 6, 3, 2);
    SetTextStyle(TriplexFont, HorizDir, UserCharSize);
    OutTextXY(GetMaxX div 2, GetMaxY div 2-40, '#GENURAY4 - Intersections');
end;

begin
   Init;
   Frame;
   MessageFrame('GENUARY 2023 - DAY 4 PROMPT - Intersections');
   {DoArt;
   FillEllipsePlay;  }
   WelcomeScreen;
   RandBarPlay;
   CloseGraph;
   RestoreCrtMode;
   Writeln('The End.');
end.
