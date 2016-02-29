% HELP
% Measure with 2.5 MHz accuracy to fit ref files ! 
% Change step size in inter_refDipole.m file
% Calib must be 900 to 1000, both included
% Call the file 900RefDipole.trx
% save in Calib folder

function[]=main()

clear;clc;

file500='Calib\500RefDipole.trx';
[CalTable1]=calib_per_Frange(500,file500);
file600='Calib\600RefDipole.trx';
[CalTable2]=calib_per_Frange(600,file600);
file700='Calib\700RefDipole.trx';
[CalTable3]=calib_per_Frange(700,file700);
file800='Calib\800RefDipole.trx';
[CalTable4]=calib_per_Frange(800,file800);
file900='Calib\900RefDipole.trx';
[CalTable5]=calib_per_Frange(900,file900);
file1800='Calib\1800RefDipole.trx';
[CalTable6]=calib_per_Frange(1800,file1800); 
file2050='Calib\2050RefDipole.trx';
[CalTable7]=calib_per_Frange(2050,file2050); 
file2450='Calib\2450RefDipole.trx';
[CalTable8]=calib_per_Frange(2450,file2450); 

%%missing values from 2230 to 2280. on mets 6.3 au milieu !fitted value!
homeCal(1:100,1)=1;
homeCal(1:100,2)=2230:0.5:2279.5;
homeCal(1:100,3)=-6.3;

homeCal2(1:61,1)=1;
homeCal2(1:61,2)=2670:0.5:2700;
homeCal2(1:61,3)=-6.3 %!fitted value!

Cal_tableLB=vertcat(CalTable1,CalTable2,CalTable3,CalTable4,CalTable5);
Cal_tableHB=vertcat(CalTable6,CalTable7,homeCal,CalTable8,homeCal2);
save Cal_tableLB
save Cal_tableHB
f='calib done'
end


function [Cal_tableFreq]=calib_per_Frange(Freq,file)

dat=dlmread(file,'',36,0);

L=1;n=1;
maxL=length(dat(:,1))-120 %chunks of 120 samples for 1 freq
%if Freq==700, maxL=length(dat(:,1))-348;end
%if Freq==800, maxL=length(dat(:,1))-464;end
%if Freq==900, maxL=length(dat(:,1))-398;end
if Freq==2050, maxL=length(dat(:,1))-120;end%-8*120; end LES POINTS EN TROP SONT ALEATOIRES !!!
%if Freq==2450, maxL=length(dat(:,1))-69*120; end % completement au pif, 
%juste pour arranger le pb. il faudrait essayer de mesurer par tranche de
%100 Mhz et voir pq il y a des points en trop !!!!
maxL
for k=L:120:maxL
    eff(n)=Calib(k,dat);
    n=n+1;
end

% Il y a un pb: eff a 807 col qd freq n' en a que 800. Je pense que tous les
% 100 MHz, il y a une valeur en double. Pour low-band, je mesure que 100
% MHz et retire la derniere valeur donc ca marche mais pour 400 MHz, j'ai 7
% valeurs de trop. Provisoire: je les enleve avec la ligne du dessus: 
% maxL=length(dat(:,1))-8*120; C'est juste 6 valeurs avec 0.5 MHz step


% read freq
fid=fopen(file); f=textscan(fid, '%f %f %f %f %s', 1, 'delimiter', '\n', 'headerlines', 15);
fmin=f{1,3}; fmax=f{1,4}; fstep=f{1,2}-1; % for having 0.5 MHz step, fstep needs to be 200 in the low band measurements (chunks of 100 MHz: 700 to 799)
step =(fmax/10^6-fmin/10^6)/(fstep);
f=fmin/10^6:step:fmax/10^6-step;
if step ~= 0.5, fprintf(strcat('You have not used 0.5 MHz step for calibration in file ',num2str(Freq),' MHz! \n')), end

[exp_eff]=interp_refDipole(Freq,step);

% plot ref values
length(eff)
length(exp_eff)
figure('Name',num2str(Freq)); plot(f',exp_eff,'r',f',eff,'b');

Cal_tableFreq(:,1)=L:120:maxL; % Line to start the block of 120. We dont put the last freq: it will be the first frequency of the next chunk/table
Cal_tableFreq(:,2)=fmin/10^6:step:fmax/10^6-step; % for this given freq
Cal_tableFreq(:,3)= exp_eff-eff; % offset=exp_eff-eff_dB

%realEff = satimo-offset
end

%% EFFICIENCY % 120 lines per frequency

function [eff_dB]=Calib(L,dat) % passing line number (=freq) and data from file
Hpol_sphere=dat(L:L+120,1).^2+dat(L:L+120,2).^2; % power
Vpol_sphere=dat(L:L+120,3).^2+dat(L:L+120,4).^2; % power
theta= ([24*2*pi/360/2:24*2*pi/360:2*pi-24*2*pi/360/2])';

m=1;
Hpol_sphere_int=0;
 
for i=1:1:length(Hpol_sphere)
    Hpol_sphere_int=Hpol_sphere_int+(Hpol_sphere(i)+Vpol_sphere(i))*sin(theta(floor(i/15)+1));  
end

eff=Hpol_sphere_int*2*pi/15*pi/8;
eff_dB=10*log10(eff);
end