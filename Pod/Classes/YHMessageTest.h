//
//  YHMessageTest.h
//  Pods
//
//  Created by baidu on 2016/11/23.
//
//

#import <Foundation/Foundation.h>

@interface YHMessageTest : NSObject
+ (void) reportSendMessage:(int64_t)msgID;
+ (void) reportReciveMessage:(int64_t)msgID;
+ (void) reportUIReciveMessage:(int64_t)msgID;
+ (void) reportServerCacheRecive:(int64_t)msgID;
@end
