import espCamAccess
import face_recgn2

def main():
        addr, pw = espCamAccess.getCreds()
        print(f"Address: {addr}, PW: {pw}")
        espCamAccess.accessCam(addr, pw)
        namesDict = face_recgn2.checkImg()
        recognised = max(zip(namesDict.values(), namesDict.keys()))[1]
        if recognised != 'Unknown':
            espCamAccess.openLock(addr, pw)
        return

if __name__ == '__main__':
        while True:
                main()
