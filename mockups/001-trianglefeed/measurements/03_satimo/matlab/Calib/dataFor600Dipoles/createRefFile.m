clear;
clc;
%% 600 File
%vna meas where the device is in port 2 and i took every 1 MHz in dB. You only need
%every 5 MHz normally. I took all the way from 500 MHz to 1 GHz, you only need up to 700
%MHz.
vna=dlmread('C:\Users\scdb\Documents\MATLAB\SAtimo\Calib\dataFor600Dipoles\600.s2p','',5,0);
k=1;
for i=101:5:205
    f(k)=vna(i,1);
    s11dB(k)=vna(i,8);
    k=k+1;
end

mat(:,1)=f';mat(:,2)=s11dB';

mat(:,3)=10.^(mat(:,2)./20); % s11 in linear
mat(:,4)=-10*log10(1-mat(:,3).*mat(:,3)); %mismatch loss in dB
mat(:,5)=-0.3; %rad eff in dB
mat(:,6)=mat(:,5)-mat(:,4);

reffile(:,1)=mat(:,1)/10^6;reffile(:,2)=mat(:,2);reffile(:,3)=0;reffile(:,4)=mat(:,6);

fileID = fopen('HomeRef600.ref','w');
fprintf(fileID,'Reference for Data 600 \r\n freq MHz \r\n s11 dB \r\n gain unknown \r\n estim eff dB \r\n');
fprintf(fileID,'%f %f %f %f \r\n',reffile');
fclose(fileID);

%% 500 file
%vna meas where the device is in port 2 and i took every 1 MHz in dB. You only need
%every 5 MHz normally. I took all the way to 1 GHz, you only need up to 600
%MHz.
vna=dlmread('C:\Users\scdb\Documents\MATLAB\SAtimo\Calib\dataFor600Dipoles\500.s2p','',5,0);
k=1;
for i=1:5:105
    f(k)=vna(i,1);
    s11dB(k)=vna(i,8);
    k=k+1;
end
mat(:,1)=f';mat(:,2)=s11dB';

mat(:,3)=10.^(mat(:,2)./20); % s11 in linear
mat(:,4)=-10*log10(1-mat(:,3).*mat(:,3)); %mismatch loss in dB
mat(:,5)=-0.3; %rad eff in dB
mat(:,6)=mat(:,5)-mat(:,4);

reffile(:,1)=mat(:,1)/10^6;reffile(:,2)=mat(:,2);reffile(:,3)=0;reffile(:,4)=mat(:,6);

fileID = fopen('HomeRef500.ref','w');
fprintf(fileID,'Reference for Data 500 \r\n freq MHz \r\n s11 dB \r\n gain unknown \r\n estim eff dB \r\n');
fprintf(fileID,'%f %f %f %f \r\n',reffile');
fclose(fileID);


