function [f,effdB]=main(file,band)
%%%%%%%%%%%%%%%%%%%%
%%%%%% USER %%%%%%%%
%%%%%%%%%%%%%%%%%%%%
%file='C:\Users\scdb\Documents\MATLAB\SAtimo\600Demo1\600Demo_topAnt_at700.trx';
%file='C:\Users\scdb\Desktop\samCA.trx';
if band == 'H'
load Cal_tableHB.mat % If meas [1700 2700]
Cal_table=Cal_tableHB;
elseif band =='L'
load Cal_tableLB.mat % If meas [700 1000]
Cal_table=Cal_tableLB; 
end
%%%%%%%%%%%%%%%%%%%%
%%%%%% STOP %%%%%%%%
%%%%%%%%%%%%%%%%%%%%
 
dat=dlmread(file,'',36,0); 

L=1;n=1;
maxL=length(dat(:,1))-120; %80 samples, every 2.5 MHz

for k=L:120:maxL
    Sat_effdB(n)=Sat_measEff(k,dat);
    n=n+1;
end
 
 % read freq
 fid=fopen(file); f=textscan(fid, '%f %f %f %f %s', 1, 'delimiter', '\n', 'headerlines', 15);
 fmin=f{1,3};fmax=f{1,4};fstep=f{1,2}-1;step =(fmax/10^6-fmin/10^6)/(fstep);
 f=fmin/10^6:step:fmax/10^6-1;

 % eff
 for ind=1:1:length(f)
     [is,row]=ismember(f(ind),Cal_table(:,2))
     effdB(ind)=Sat_effdB(ind)+Cal_table(row,3);
 end

figure('Name',file);
set( axes('FontSize',14))
plot(f',effdB);hold on;
xlabel('Frequency [MHz]','interpreter','latex','FontSize',14);
ylabel('$\eta_{T}$ [dB]','interpreter','latex','FontSize',14);
end

function [effdB]=Sat_measEff(L,dat)

Hpol_sphere=dat(L:L+120,1).^2+dat(L:L+120,2).^2; % power
Vpol_sphere=dat(L:L+120,3).^2+dat(L:L+120,4).^2; % power
theta= ([24*2*pi/360/2:24*2*pi/360:2*pi-24*2*pi/360/2])';

m=1;
Hpol_sphere_int=0;
 
for i=1:1:length(Hpol_sphere)
    Hpol_sphere_int=Hpol_sphere_int+(Hpol_sphere(i)+Vpol_sphere(i))*sin(theta(floor(i/15)+1));  
end

eff=Hpol_sphere_int*2*pi/15*pi/8;
effdB=10*log10(eff);
end
