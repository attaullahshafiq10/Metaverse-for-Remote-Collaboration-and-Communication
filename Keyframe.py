# Keyframe Animation Algorithm


class Keyframe:
    def __init__(self, time, position, rotation):
        self.time = time
        self.position = position
        self.rotation = rotation

class Animation:
    def __init__(self, keyframes):
        self.keyframes = keyframes
    
    def evaluate(self, time):
        # Find the two keyframes that surround the current time
        kf1 = None
        kf2 = None
        for kf in self.keyframes:
            if kf.time <= time:
                kf1 = kf
            else:
                kf2 = kf
                break
        if kf1 is None:
            return self.keyframes[0].position, self.keyframes[0].rotation
        if kf2 is None:
            return self.keyframes[-1].position, self.keyframes[-1].rotation
        
        # Interpolate between the two keyframes
        t = (time - kf1.time) / (kf2.time - kf1.time)
        position = kf1.position + t * (kf2.position - kf1.position)
        rotation = kf1.rotation + t * (kf2.rotation - kf1.rotation)
        return position, rotation
