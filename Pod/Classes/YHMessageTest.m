//
//  YHMessageTest.m
//  Pods
//
//  Created by baidu on 2016/11/23.
//
//

#import "YHMessageTest.h"
#import "DZURLRoute.h"
#import "DZLogger.h"
static NSString* const kBaseURL = @"http://172.24.102.137:5000";
@implementation YHMessageTest

+ (void) reportSendMessage:(int64_t)msgID
{
    [self report:@"reportsend" messageID:msgID];
}

+ (void) reportReciveMessage:(int64_t)msgID
{
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1 * NSEC_PER_SEC)), dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^{
        [self report:@"reportrecive" messageID:msgID];
    });
}

+ (void) reportUIReciveMessage:(int64_t)msgID
{
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1 * NSEC_PER_SEC)), dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^{
        [self report:@"reportuirecive" messageID:msgID];
    });
}
+ (void) reportServerCacheRecive:(int64_t)msgID
{
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(1 * NSEC_PER_SEC)),  dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_HIGH, 0), ^{
        [self report:@"reportcacherecive" messageID:msgID];
    });
}
+ (void) report:(NSString*)method messageID:(int64_t)msgID
{
    
    NSString* str = [NSString stringWithFormat:@"%@/%@",kBaseURL, method];
    NSURL* url = DZURLRouteQueryLink(str, @{
                                                 @"msgID":@(msgID)
                                                 });
    NSURLSession* session = [NSURLSession sharedSession];
    NSURLSessionDataTask* task = [session dataTaskWithURL:url completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {
        
        if (error) {
            DDLogError(@"%@", error);
        } else {
            NSString* string = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
            DDLogInfo(@"GET RESPONSE %@", string);
        }
    }];
    [task resume];
}

@end
