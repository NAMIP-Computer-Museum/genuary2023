10 MODE 0
20 INK 0,1
30 BORDER 1
40 FOR I=2 TO 15:INK I,I+2:NEXT I
50 CLS
60 HN$="HAPPY 2023!":SZ=2:DC=0:GOSUB 130
70 HN$=" ` NAM-IP MUSEUM d":SZ=1:DC=4:GOSUB 130
80 HN$="#GENUARY retro style":SZ=0:DC=6:GOSUB 130
90 GOTO 90
100 REM ==================
110 REM    DRAW CHARS
120 REM ==================
130 FOR I=1 TO LEN(HN$)
140 PEN ((I+DC-1) MOD 15)+1:LOCATE I,25
160 PRINT MID$(HN$,I,1)
170 NEXT I
180 PEN 1
190 IF SZ=0 THEN RETURN
200 FOR Y=0 TO 14 STEP 2
210 FOR X=1 TO LEN(HN$)*32 STEP 4
220 C=TEST(X,Y)
230 IF SZ=1 THEN X1=X+40:Y1=100+Y*2:SX=1:SY=2:GOSUB 320
240 IF SZ=2 THEN X1=4*X:Y1=320+4*Y:SX=4:SY=4:GOSUB 320
250 NEXT X
260 NEXT Y
270 LOCATE 1,1
280 RETURN
290 REM =============
300 REM BIG PIXEL
310 REM =============
320 IF C=0 THEN RETURN
330 FOR K=0 TO SY-1
340 IF X1>640 THEN X1=X1-768:Y1=Y1-100
350 MOVE X1,Y1+K:DRAWR SX*4-4,0,C
360 NEXT K
370 RETURN
400 FOR I=128 TO 255:PRINT I,CHR$(I):NEXT I
