import numpy as np
import matplotlib.pyplot as plt
num=501
def sigmoid(x): return 1 / (1 + np.exp(-x))
x=np.linspace(-20,20,num)
x=x.reshape(1,num)
y=np.zeros((1,num))
half_step=0.15
rotation_angle=-1*np.pi/180
rot_matrix=np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],[np.sin(rotation_angle),np.cos(rotation_angle)]])
for i in range(0,x.shape[1]):
    y[0,i]=sigmoid(x[0,i])
    # if x[0,i]<-half_step:
    #     y[0,i]=0
    # elif x[0,i]>half_step:
    #     y[0,i]=1
    # else:
    #     y[0,i]=1/(2*half_step)*x[0,i]+0.5
position_before_rot=np.vstack((x[0,:],y[0,:]))
position_after_rot=np.dot(rot_matrix, position_before_rot)
fig=plt.figure()
plt.subplot(4,1,1)
plt.plot(x[0,:],y[0,:])
plt.title('Real height of the IZO film')
plt.subplot(4,1,2)

plt.plot(position_after_rot[0,:],position_after_rot[1,:])
plt.plot(position_after_rot[0,0],position_after_rot[1,0],'bo')
plt.text(-21,0.5,'start point')
plt.plot(position_after_rot[0,120],position_after_rot[1,120],'go')
plt.text(-11,0.5,'good window')
plt.plot(position_after_rot[0,220],position_after_rot[1,220],'ro')
plt.text(-3,0.5,'bad window')
plt.title('Measured height because of the rotation of the measuring platform')
k_good=(position_after_rot[1,0]-position_after_rot[1,120])/(position_after_rot[0,0]-position_after_rot[0,120])
# k=(0.08870-0.17453)/(-10.1596+19.99924)
angle_calculated=-np.arctan(k_good)
restore_matrix=np.array([[np.cos(angle_calculated), -np.sin(angle_calculated)],[np.sin(angle_calculated),np.cos(angle_calculated)]])
restored_position=np.dot(restore_matrix, position_after_rot)
plt.subplot(4,1,3)
plt.plot(restored_position[0,:],restored_position[1,:])
plt.title('Restored height (good window)')

k_bad=(position_after_rot[1,0]-position_after_rot[1,220])/(position_after_rot[0,0]-position_after_rot[0,220])
# k=(0.08870-0.17453)/(-10.1596+19.99924)
angle_calculated=-np.arctan(k_bad)
restore_matrix=np.array([[np.cos(angle_calculated), -np.sin(angle_calculated)],[np.sin(angle_calculated),np.cos(angle_calculated)]])
restored_position=np.dot(restore_matrix, position_after_rot)
plt.subplot(4,1,4)
plt.plot(restored_position[0,:],restored_position[1,:])
plt.title('Restored height (bad window)')
plt.show()
fig.savefig("E:/Files/Year4/Year4.2/OptoDevFab/lab_reports/lab1/template/8.png", dpi=600, format=None, metadata=None,
            bbox_inches=None, pad_inches=0.1,
            facecolor='auto', edgecolor='auto',
            backend=None
            )