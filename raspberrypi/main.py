import espCamAccess
import face_recgn2
import time

def getConn():
                time.sleep(1)
                addr, pw = espCamAccess.getCreds()
                if pw == 'DINGDONG':
                        return
                print(f"Address: {addr}, PW: {pw}")
                if (espCamAccess.readLine() == 'DINGDONG'):
                        espCamAccess.accessCam(addr, pw)
                        namesDict = face_recgn2.checkImg()
                        flag=0                          # Try improving logic for seeing if
                        for value in namesDict.values():  # all values are zero
                                if value != 0:
                                        flag = 1
                        if flag == 1:
                                recognised = max(zip(namesDict.values(), namesDict.keys()))[1]
                        else:
                                recognised = 'Unknown'
                        print(f"Recognised as {recognised}!")
                        if recognised != 'Unknown':
                                espCamAccess.openLock(addr, pw)
                                time.sleep(.25)
                                print("Unlocked!")
                        print("Logging out..")
                        espCamAccess.logout(addr)
                        print("Logged out!")
                        return

def main():
        while(1):
                time.sleep(2)
                print("Fetching new connection..")
                getConn()

if __name__ == '__main__':
        time.sleep(3)
        main()
