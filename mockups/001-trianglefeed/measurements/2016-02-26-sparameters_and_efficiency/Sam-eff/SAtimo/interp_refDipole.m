function [exp_eff_interp]=interp_refDipole(freq,step)
%recommended : step = 0.5 for low band and for high band

if freq==900
% 995 to 900
exp_eff=dlmread('Calib\SD900-51.ref', '', [25 3 45 3]);
fr_original=900:5:1000;
fr_accurate=900:step:1000-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);
%plot(fr_original,exp_eff,'o',fr_accurate,exp_eff_interp);

elseif freq==800
% 895 to 800
exp_eff=dlmread('Calib\SD850-02.ref', '', [15 3 35 3]);
fr_original=800:5:900;
fr_accurate=800:step:900-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);
%plot(fr_original,exp_eff,'o',fr_accurate,exp_eff_interp);

elseif freq==700
% 795 to 700
ii=1;
for i=36:5:136
    exp_eff(ii)=dlmread('Calib\SD740-70.ref', '', [i 2 i 2]);
    ii=ii+1;
end
fr_original=700:5:800;
fr_accurate=700:step:800-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);
%plot(fr_original,exp_eff,'o',fr_accurate,exp_eff_interp);

elseif freq==600
% 695 to 600
exp_eff=dlmread('Calib\HomeRef600.ref', '', [5 3 25 3]);
fr_original=600:5:700;
fr_accurate=600:step:700-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);
%plot(fr_original,exp_eff,'o',fr_accurate,exp_eff_interp);

elseif freq==500
% 595 to 500
exp_eff=dlmread('Calib\HomeRef500.ref', '', [5 3 25 3]);
fr_original=500:5:600;
fr_accurate=500:step:600-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);
%plot(fr_original,exp_eff,'o',fr_accurate,exp_eff_interp);

elseif freq==1800
% 1600 to 1830 (461 points)
exp_eff=dlmread('Calib\SD1800-45.ref', '', [5 3 51 3]);
fr_original=1600:5:1830;
fr_accurate=1600:step:1830-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);

elseif freq==2050
% 1830 to 2230
exp_eff=dlmread('Calib\SD2050-36.ref', '', [5 3 85 3]);
fr_original=1830:5:2230;
fr_accurate=1830:step:2230-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);


elseif freq==2450
% 2280 to 2670
exp_eff=dlmread('Calib\SD2450-43.ref', '', [5 3 83 3]);
fr_original=2280:5:2670;
fr_accurate=2280:step:2670-step;
exp_eff_interp=interp1(fr_original,exp_eff,fr_accurate);

end
end